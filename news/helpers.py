import os
import uuid


# Hàm random tên hình ảnh
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('news/images/article', filename)
