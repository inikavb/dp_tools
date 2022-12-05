# import lines


def check_final_outputs(entry : path):
    """ makes sure outputs exist and checks formatting """

    if not any(output_file.endswith(entry) for output_file in output_files_present):
        code = FlagCode.HALT
        message = "An output file named or ending with '" + str(entry) + "' was expected but not found in " + str(final_outputs_dir) + "."
    else:
        code = FlagCode.GREEN
        message = "The expected output file named or ending with '" + str(entry) + "' was found in " + str(final_outputs_dir) + "."

    return {"code": code, "message": message}
  
def check_for_processing_tar(entries:path):
    """ this just makes sure a processing tar exists and at least has the Snakefile, as its contents can vary quite a bit """

    target_substring = str(output_prefix).rstrip("-") + "/Snakefile"

    base_target = "/Snakefile"

    if not any(target_substring.lower() in string.lower() for string in entries):

        if not any(base_target.lower() in string.lower() for string in entries):
            code = FlagCode.HALT
            message = "The '" + processing_tar_file + "' does not have a 'Snakefile' as expected."
        
    else:
        code = FlagCode.GREEN
        message = "The '" + processing_tar_file + "' contains the expected 'Snakefile.'"

    return {"code": code, "message": message}
  
def check_intermediate_log_files_filtered(entry : path):
    
    output_files_present = [f for f in os.listdir(filtered_reads_dir) if os.path.isfile(os.path.join(filtered_reads_dir, f))]
    if not any(output_file.endswith(entry) for output_file in output_files_present):
        code = FlagCode.HALT
        message = "An output file named or ending with '" + str(entry) + "' was expected but not found in " + str(filtered_reads_dir) + "."
    else:
        code = FlagCode.GREEN
        message = "The expected output file named or ending with " + str(entry) + " was found."

    return {"code": code, "message": message}
  
def check_intermediate_log_files_trimmed(entry : path):

    output_files_present = [f for f in os.listdir(trimmed_reads_dir) if os.path.isfile(os.path.join(trimmed_reads_dir, f))]
    if not any(output_file.endswith(entry) for output_file in output_files_present):
        code = FlagCode.HALT
        message = "An output file named or ending with '" + str(entry) + "' was expected but not found in " + str(trimmed_reads_dir) + "."
        
    else: 
        code = FlagCode.GREEN
        message = "The expected output file named or ending with " + str(entry) + " was found."

    return {"code": code, "message": message}
  
def read_samples(file_path):
    """ reading unique sample names into list """

    with open(file_path) as f:
        sample_names = f.read().splitlines()

    return(sample_names)
