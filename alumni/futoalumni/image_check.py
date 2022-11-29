
def check_file_extension(file):
    """
        checks the extension being used
        1.can be imported in the view function to check the file type before validating form
        2. if uploading multiple files, override the post method to, loop through the files to check the file type
    
    """

    extensions = {
        'images' : ('jpeg', 'jpg', 'png', 'gif'),
    }
    file = str(file)
    fil = file.split('.')[1]
    for x in extensions.values():
        if fil in x:
            return file
        return None
file_ext = check_file_extension




def item_files_directory(instance,filename):
   
    return f'{instance.firstname}/{filename}'
passport_uploads = item_files_directory


def business_files_directory(instance,filename):
   
    return f'{instance.name}/{filename}'
business_uploads = business_files_directory


