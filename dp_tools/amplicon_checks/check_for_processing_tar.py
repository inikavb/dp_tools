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
