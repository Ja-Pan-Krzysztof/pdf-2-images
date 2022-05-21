from pdf2image import convert_from_path
from img2pdf import convert
import os
from pathlib import Path


class ConvertToImgs:
    _popper = r'E:/Python/..Python_venv/pdf2img/Lib/site-packages/poppler-0.68.0/bin'

    def __init__(self, path: str, resolution: int, directory: str = None):
        self.path = path
        self.resolution = resolution

        self.directory = directory

    def main(self):
        path = Path().resolve()

        if not os.path.exists(f'{path}/cache'):
            os.mkdir('cache')

        images = convert_from_path(self.path, self.resolution, poppler_path=self._popper)

        if self.directory is None:
            for i, image in enumerate(images):
                image.save(f'{i}.png')

        else:
            if not os.path.exists(f'{path}/{self.directory}'):
                os.mkdir(f'{self.directory}')

            for i, image in enumerate(images):
                image.save(f'{self.directory}/{i}.png')

        cache_path = f'{path}\\cache'

        if os.path.exists(f'{cache_path}'):
            files = os.listdir(f'{cache_path}')

            for file in files:
                os.remove(f'{cache_path}/{file}')


class ConventToPdf:
    def __init__(self, path_folder_imgs, pdf_name: str = 'output'):
        self.path = path_folder_imgs
        self.pdf_name = pdf_name

        self.imgs = []

        if self.pdf_name[-1: -4] != '.pdf':
            self.pdf_name = f'{self.pdf_name}.pdf'

    def main(self):
        for i in os.listdir(self.path):
            if not i.endswith(''):
                continue

            path = os.path.join(self.path, i)

            if os.path.isdir(path):
                continue

            self.imgs.append(path)

        with open(f'{self.pdf_name}', 'wb') as f:
            f.write(convert(self.imgs))

    '''def __init__(self, path_folder_imgs, pdf_name: str):
        self.fpdf = FPDF()
        self.pdf_name = pdf_name
        self.fpdf.set_auto_page_break(0)
        self.path = path_folder_imgs

    def main(self):
        img_list = [i for i in os.listdir(self.path)]

        for img in img_list:
            self.fpdf.add_page()
            self.fpdf.image(f'{self.path}/{img}')

        if self.pdf_name == '':
            self.pdf_name = 'output.pdf'

        self.fpdf.output(self.pdf_name)'''





