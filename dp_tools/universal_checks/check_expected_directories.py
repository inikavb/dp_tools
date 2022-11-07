def check_expected_directories(directory : path):
    """Checks expected directories exist
    This is achieved by checking if the 'os.path.isdire" exists given a directory.
    An optional name_reformat_function can be supplied to address sample name changes that occur in the multiqc report.
    An example being the renaming of Sample '-' characters to '_' for certain RSeQC modules.
    
    :param directory: Directory name
    :type directory: str
    :param path: MultiQC report directory
    :type path: Path
    :return: Flag Entry denoting successful or failing results. Includes description of directory names and any missing directories
    :rtype: FlagEntry
    """
    if not os.path.isdir(directory):
        code = FlagCode.HALT
        message = "The directory '" + str(directory) + "' was expected but not found."
    else: 
        code = FlagCode.GREEN
        message = "The directory " + str(directory)+ " exists."
    return {"code": code, "message": message}
