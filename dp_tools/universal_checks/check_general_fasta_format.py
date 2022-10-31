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
