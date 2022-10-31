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
