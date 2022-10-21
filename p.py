

# default params
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}


# for the dataset
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS



allowed_file('/sdfsdfskdhfjksd.csv')
