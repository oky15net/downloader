# downloader_script.py
import requests
import os
import gradio as gr

def download_file(url, download_folder="downloads"):
    if not url:
        return "URL tidak valid"
    local_filename = os.path.join(download_folder, url.split('/')[-1])
    os.makedirs(download_folder, exist_ok=True)
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return f"File berhasil diunduh: {local_filename}"
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

def create_ui():
    with gr.Blocks() as downloader:
        gr.Markdown("## File Downloader")
        url_input = gr.Textbox(label="Direct Link URL")
        download_button = gr.Button("Download")
        output = gr.Textbox(label="Download Path")

        download_button.click(fn=download_file, inputs=url_input, outputs=output)
    
    downloader.launch()

if __name__ == "__main__":
    create_ui()
