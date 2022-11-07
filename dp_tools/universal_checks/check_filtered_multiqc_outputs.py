def check_filtered_multiqc_outputs(sample : path):
    """Checks the filtered multiqc outputs in the multiqc report.
    This is achieved by checking the multiqc outputs in the multiqc report (Change this w more specific language).
    
    :param sample: Query sample names to check for presence in multiqc outputs
    :type sample: list[str]
    :param path: MultiQC report directory
    :type path: Path
    :return: Flag Entry denoting successful or failing results. Includes description of multiqc output names and any missing outputs
    :rtype: FlagEntry
    """
    zip_file = zipfile.ZipFile(filt_multiqc_data_path)
    df = pd.read_csv(zip_file.open("multiqc_general_stats.txt"), sep = "\t", usecols = ["Sample"])
    file_prefixes_in_multiqc = df["Sample"].tolist()

    if not sample in file_prefixes_in_multiqc:
        code = FlagCode.HALT
        message = "The filtered multiqc output is missing the expected '" + sample + "' entry."
    else:
        code = FlagCode.GREEN
        message = "The filtered multiqc output contains the expected " + sample + " entry."
    return {"code": code, "message": message}
