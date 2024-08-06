# downloader_script.py
import requests
import os

def download_file(url, download_folder):
    local_filename = os.path.join(download_folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def on_ui_tabs():
    with gr.Blocks() as downloader:
        gr.Markdown("## File Downloader")
        url_input = gr.Textbox(label="Direct Link URL")
        download_button = gr.Button("Download")
        output = gr.Textbox(label="Download Path")

        def download_and_show(url):
            download_folder = "downloads"
            os.makedirs(download_folder, exist_ok=True)
            file_path = download_file(url, download_folder)
            return file_path

        download_button.click(fn=download_and_show, inputs=url_input, outputs=output)
    return [(downloader, "Downloader", "downloader")]

script_callbacks.on_ui_tabs(on_ui_tabs)
