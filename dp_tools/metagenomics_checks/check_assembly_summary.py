def check_assembly_summary(assembly_summary_path:path):
    # making sure assembly summary file is there

    if not os.path.exists(assembly_summary_path):
        code =  FlagCode.HALT
        message = "The assembly summary file, " + str(assembly_summary_path) + ", is expected but was not found."
    else: 
        code = FlagCode.GREEN
        message = "The assembly summary file, " + str(assembly_summary_path) + ", was found."
    return {"code": code, "message": message}
