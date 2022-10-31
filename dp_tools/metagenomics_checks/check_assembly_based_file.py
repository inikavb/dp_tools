def check_assembly_based_file(sample : path, file: path, failed_assemblies_list: path ,assembly = True):
    
    if not os.path.exists(file):
        code = FlagCode.HALT
        message = "The expected file '" + str(file) + "' does not exist."
    else: 
        if not os.path.getsize(file) > 0:
            # a sample can have no genes called even if the assembly produced contigs, so this is only throwing a warning if we are checking an assembly here
            if sample not in failed_assemblies_list and assembly == True:
                code = FlagCode.HALT
                message = "The file '" + str(file) + "' is empty, but that sample isn't noted in the 'Failed-assemblies.tsv' file as it should be if the assembly failed."
            elif sample in failed_assemblies_list and assembly == True:
                code = FlagCode.YELLOW
                message = "The file '" + str(file) + "' is exists and is noted in the 'Failed-assemblies.tsv' file as it should be if the assembly failed."
        else: 
            code = FlagCode.GREEN
            message = "The file '" + str(file) + "' exists and contains content."
    return {"code": code, "message": message}
