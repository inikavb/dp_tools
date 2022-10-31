def check_log_files(entry : path):

    ## filtered
    output_files_present = [f for f in os.listdir(filtered_reads_dir) if os.path.isfile(os.path.join(filtered_reads_dir, f))]

    if not any(output_file.endswith(entry) for output_file in output_files_present):
        code = FlagCode.HALT
        message = "An output file named or ending with '" + str(entry) + "' was expected but not found in " + str(filtered_reads_dir) + "."
    else:
        code = FlagCode.GREEN
        message = "The expected output file named or ending with " + str(entry) + " was found in " + str(filtered_reads_dir) + "."
    return {"code": code, "message": message} 
