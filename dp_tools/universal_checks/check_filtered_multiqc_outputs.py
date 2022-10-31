def check_filtered_multiqc_outputs(sample : path):
    # checking filtered
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
