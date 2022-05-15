from pdf2image import convert_from_path
import os
from pathlib import Path


class Convert:
    _popper = r'E:/Python/..Python_venv/pdf2img/Lib/site-packages/poppler-0.68.0/bin'

    def __init__(self, path: str, resolution: int, directory: str = None):
        self.path = path
        self.resolution = resolution

        self.directory = directory

    def main(self):
        path = Path().resolve()

        if not os.path.exists(f'{path}/cache'):
            os.mkdir('cache')

        images = convert_from_path(self.path, self.resolution, poppler_path=self._popper, output_folder='cache/')

        if self.directory is None:
            for i, image in enumerate(images):
                image.save(f'{i}.png')

        else:
            for i, image in enumerate(images):
                image.save(f'{self.directory}/{i}.png')

        cache_path = f'{path}\\cache'

        if os.path.exists(f'{cache_path}'):
            files = os.listdir(f'{cache_path}')

            for file in files:
                os.remove(f'{cache_path}/{file}')
