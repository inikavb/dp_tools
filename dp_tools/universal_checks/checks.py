def check_expected_directories(directory : path):
    """Checks expected directories exist
    This is achieved by checking if the 'os.path.isdire" exists given a directory.
    An optional name_reformat_function can be supplied to address sample name changes that occur in the multiqc report.
    An example being the renaming of Sample '-' characters to '_' for certain RSeQC modules.
    
    :param directory: Directory name
    :type directory: str
    :param path: MultiQC report directory
    :type path: Path
    :return: Flag Entry denoting successful or failing results. Includes description of directory names and any missing directories
    :rtype: FlagEntry
    """
    if not os.path.isdir(directory):
        code = FlagCode.HALT
        message = "The directory '" + str(directory) + "' was expected but not found."
    else: 
        code = FlagCode.GREEN
        message = "The directory " + str(directory)+ " exists."
    return {"code": code, "message": message}
  
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
  
def check_for_file_and_contents(file: path):
    """Used by check_fastq_files and check_final_outputs functions to confirm existence of files and that they hold content.
    This is achieved by checking the file name's existence and whether it holds content (make more specific later).
    
    :param file: Sample file names to check for presense
    :type file: str
    :param path: path of directory
    :type path: Path
    :return: Flag Entry denoting successful or failing results. Includes name of sample files and any missing sample files
    :rtype: FlagEntry
    """
    if os.path.exists(file): # path exists
            # now checking for content
            if not os.path.getsize(file) > 0: # file is empty
                code = FlagCode.HALT
                message = "The file " + str(file) + " exists, but the file is empty."
            else:
                code = FlagCode.GREEN # path exists and holds content
                message = "The file " + str(file) + " exists and holds content."
    else:
        code = FlagCode.HALT
        message = "The expected file '" + str(file) + "' does not exist."
    return {"code": code, "message": message}
  
def check_general_fasta_format(file : path):

    line_num = 0
    num_headers = 0
    num_seqs = 0

    with open(file) as in_file:

        for line in in_file:

            # keeping track of current line for reporting any problems
            line_num += 1

            if line.strip().startswith(">"):
                num_headers += 1
            else:
                num_seqs += 1

            if num_headers != num_seqs + 1 and num_headers != num_seqs:
                code = FlagCode.HALT
                message = "Fasta file '" + str(file) + "' does not seem to be formatted properly. Problem detected at line " + str(line_num) + "."
            else:
                code = FlagCode.GREEN
                message = "Fasta file " + str(file) + " is formatted properly."
    return {"code": code, "message": message}
  
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
