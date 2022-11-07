def check_for_file_and_contents(file: path):
    """Used by check_fastq_files and check_final_outputs functions to confirm existence of files and that they hold content.
    This is achieved by checking the file name's existence and whether it holds content (make more specific later).
    
    :param file: Sample file names to check for presense
    :type file: str
    :param path: path of directory
    :type path: Path
    :return: Flag Entry denoting successful or failing results. Includes name of sample files and any missing sample files
    :rtype: FlagEntry
    """
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
