def check_for_file_and_contents(file: path):
    """ used by check_fastq_files and check_final_outputs functions """

    if os.path.exists(file): # path exists
            # now checking for content
            if not os.path.getsize(file) > 0: # file is empty
                code = FlagCode.HALT
                message = "The file " + str(file) + " exists, but the file is empty."
            else:
                code = FlagCode.GREEN # path exists and holds content
                message = "The file " + str(file) + " exists and holds content."
    else:
        code = FlagCode.HALT
        message = "The expected file '" + str(file) + "' does not exist."
    return {"code": code, "message": message} 
