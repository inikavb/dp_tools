def check_processing_tar(entries:path,item:path):
    """ this makes sure a processing tar exists and contains what we expect """
    if entries[0] + item not in entries:
        code=FlagCode.HALT
        message = "The '" + str(processing_tar_file) + "' does not have '" + str(item) + "' as expected."
    else:
        code=FlagCode.GREEN
        message="The '" + str(processing_tar_file) + "' contains the expected '" + str(item) + "'."
    return {"code": code, "message": message}
