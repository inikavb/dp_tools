# imports

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
    
  
def check_assembly_based_overview_table(expected_samples: path, overview_table_path:path):
    """ makes sure the output table exists and all input samples are in it """

    # now making sure all samples are in there
    # reading in table and getting sample IDs in list
    overview_tab = pd.read_csv(overview_table_path, sep = "\t")
    samples_in_tab = overview_tab['Sample_ID'].tolist()

    missing_sample_IDs = []

    for sample in expected_samples:
        if sample not in samples_in_tab:
            missing_sample_IDs.append(sample)

    if len(missing_sample_IDs) > 0:
        code=FlagCode.HALT
        message="The assembly overview table, '" + overview_table_path + "', doesn't have all the samples expected to be there."
    else:
        code=FlagCode.GREEN
        message="The assembly overview table, '" + overview_table_path + "', contains all the expected samples."
    return {"code": code, "message": message}
    
def check_assembly_summary(assembly_summary_path:path):
    # making sure assembly summary file is there

    if not os.path.exists(assembly_summary_path):
        code =  FlagCode.HALT
        message = "The assembly summary file, " + str(assembly_summary_path) + ", is expected but was not found."
    else: 
        code = FlagCode.GREEN
        message = "The assembly summary file, " + str(assembly_summary_path) + ", was found."
    return {"code": code, "message": message}
    
def check_bins_dir(output_files_present:path):
    """ makes sure outputs exist and checks formatting """

    ## bins_dir ##

    if output_files_present:

        output_fasta_bins = [filename for filename in output_files_present if filename.endswith(".fasta")]

        # checking for contents (checking fasta format not straightforward when there are softwraps, but don't want to remove them on these due to large contigs)
        for bin_file in output_fasta_bins:

            curr_file_path = bins_dir + bin_file

            if not os.path.getsize(curr_file_path) > 0:
                code=FlagCode.HALT
                message="The file '" + str(curr_file_path) + "' is empty, but shouldn't be there if that's the case."
            else:
                code=FlagCode.GREEN
                message="The file '" + str(curr_file_path) + "' holds content."

        # making sure summary table is there if there are any bins
        if len(output_fasta_bins) > 0:

            bins_summary_path = bins_dir + additional_prefix + "bins-overview.tsv"

            if not os.path.exists(bins_summary_path):
                code=FlagCode.HALT
                message="The bins summary file, " + str(bins_summary_path) + ", is expected but was not found."
            else:
                code=FlagCode.GREEN
                message="The file '" + str(bins_summary_path) + "' holds content."
    return {"code": code, "message": message}
    
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
    
def check_mags_dir(output_files_present:path):
    ## MAGs_dir ##

    if output_files_present:

        output_fasta_MAGs = [filename for filename in output_files_present if filename.endswith(".fasta")]

        # checking for contents (checking fasta format not straightforward when there are softwraps, but don't want to remove them on these due to large contigs)
        for MAG_file in output_fasta_MAGs:

            curr_file_path = MAGs_dir + MAG_file

            if not os.path.getsize(curr_file_path) > 0:
                code=FlagCode.HALT
                message= "The file '" + str(curr_file_path) + "' is empty, but shouldn't be there if that's the case."
            else:
                code=FlagCode.GREEN
                message="The file '" + str(curr_file_path) + "' holds content."

        # making sure summary table is there if there are any bins
        output_fasta_bins = [filename for filename in output_files_present if filename.endswith(".fasta")]
        if len(output_fasta_bins) > 0:

            MAGs_summary_path = MAGs_dir + additional_prefix + "MAGs-overview.tsv"

            if not os.path.exists(MAGs_summary_path):
                code = FlagCode.HALT
                message = "The MAGs summary file, " + str(MAGs_summary_path) + ", is expected but was not found."
            else:
                code=FlagCode.GREEN
                message="The file '" + str(MAGs_summary_path) + "' holds content."

    return {"code": code, "message": message}
    
    
 def check_processing_tar(entries:path,item:path):
    """ this makes sure a processing tar exists and contains what we expect """
    if entries[0] + item not in entries:
        code=FlagCode.HALT
        message = "The '" + str(processing_tar_file) + "' does not have '" + str(item) + "' as expected."
    else:
        code=FlagCode.GREEN
        message="The '" + str(processing_tar_file) + "' contains the expected '" + str(item) + "'."
    return {"code": code, "message": message}
    
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
