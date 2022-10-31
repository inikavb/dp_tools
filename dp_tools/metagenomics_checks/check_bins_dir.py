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
