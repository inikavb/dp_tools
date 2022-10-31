def check_raw_multiqc_outputs(sample : path):
    """ makes sure all samples' read files are in the multiqc outputs """

    # checking raw
    zip_file = zipfile.ZipFile(raw_multiqc_data_path)
    df = pd.read_csv(zip_file.open("multiqc_general_stats.txt"), sep = "\t", usecols = ["Sample"])
    file_prefixes_in_multiqc = df["Sample"].tolist()

    if not sample in file_prefixes_in_multiqc:
        code = FlagCode.HALT
        message = "The raw multiqc output is missing the expected '" + sample + "' entry."
    else:
        code = FlagCode.GREEN
        message = "The raw multiqc output contains the expected " + sample + " entry."
    return {"code": code, "message": message} 
