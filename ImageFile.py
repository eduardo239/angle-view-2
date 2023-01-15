class ImageFile:
    def __init__(self):
        self.folder_path = None
        self.last_file = None
        self.cropped_file = None
        self.cos = 0
        self.sen = 0
        self.res = 0

    def __str__(self):
        return f"path: {self.folder_path}, last_file: {self.last_file}"
