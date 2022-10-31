def check_assembly_based_genes_file(sample : path, file: path, failed_assemblies_list :path, assembly = True):
    """ 
    separate function for working with expected output genes files, to handle
    cases where assemblies can succeed while there are still no gene calls

    just checks the file isn't empty if it exists
    """
    
    if os.path.exists(file) and sample not in failed_assemblies_list:

        if not os.path.getsize(file) > 0:
            code = FlagCode.HALT
            message = "The expected file '" + str(file) + "' exists, but appears to be empty when it shouldn't be."
        else: 
            code = FlagCode.GREEN
            message = "The expected file '" + str(file) + "' exists and holds content."
    else:
        code = FlagCode.HALT
        message = "The expected file '" + str(file) + "' is not in the failed assemblies list."
    return {"code": code, "message": message}
