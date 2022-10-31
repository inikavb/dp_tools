def check_final_outputs(entry : path):
    """ makes sure outputs exist and checks formatting """

    if not any(output_file.endswith(entry) for output_file in output_files_present):
        code = FlagCode.HALT
        message = "An output file named or ending with '" + str(entry) + "' was expected but not found in " + str(final_outputs_dir) + "."
    else:
        code = FlagCode.GREEN
        message = "The expected output file named or ending with '" + str(entry) + "' was found in " + str(final_outputs_dir) + "."

    return {"code": code, "message": message}
