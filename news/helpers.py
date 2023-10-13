import os
import uuid
import re


# Hàm random tên hình ảnh
# --> Sử dụng trong models (trường image)
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('news/images/article', filename)


def get_skip_slug_article(path):
    # Lấy phần cuối của chuỗi path --> đảm bảo slug luôn đúng kể cả trong trường hợp có thay đổi phần đầu của đường dẫn
    last_path = path.split("/")[-1]

    skip_slug = None

    match = re.search(r"^(?P<article_slug>[\w-]+)-a\d+\.html", last_path)

    if match:
        skip_slug = match.group("article_slug")

    return skip_slug
