def check_tar_log_files(samples:path):
    # checking log files
    for sample in samples:

        for suffix in expected_log_file_suffixes:

            target_log = logs_dir + sample + suffix

            if target_log not in entries:
                code= FlagCode.HALT
                message = "The '" + str(processing_tar_file) + "' does not have the '" + str(target_log) + "' log file as expected."
            else: 
                code = FlagCode.GREEN
                message = "The '" + str(processing_tar_file) + "' contains the expected '" + str(target_log) + "' log file."
    return {"code": code, "message": message}
