def check_intermediate_log_files_trimmed(entry : path):

    output_files_present = [f for f in os.listdir(trimmed_reads_dir) if os.path.isfile(os.path.join(trimmed_reads_dir, f))]
    if not any(output_file.endswith(entry) for output_file in output_files_present):
        code = FlagCode.HALT
        message = "An output file named or ending with '" + str(entry) + "' was expected but not found in " + str(trimmed_reads_dir) + "."
        
    else: 
        code = FlagCode.GREEN
        message = "The expected output file named or ending with " + str(entry) + " was found."

    return {"code": code, "message": message}
