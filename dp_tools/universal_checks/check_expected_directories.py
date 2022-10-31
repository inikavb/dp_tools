def check_expected_directories(directory : path):
    """ checks expected directories exist """

    if not os.path.isdir(directory):
        code = FlagCode.HALT
        message = "The directory '" + str(directory) + "' was expected but not found."
        #report_failure("The directory '" + str(directory) + "' was expected but not found.")
    else: 
        code = FlagCode.GREEN
        message = "The directory " + str(directory)+ " exists."
    return {"code": code, "message": message}

def read_samples(file_path):
    """ reading unique sample names into list """

    with open(file_path) as f:
        sample_names = f.read().splitlines()

    return(sample_names)
