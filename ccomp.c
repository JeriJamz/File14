#include <stdio.h>

in
main(int arhc, char **argv)
{
    FILE *infile;
    FILE *outfile;
    int ch;

    /*parse the command line(lol here we go)*/

    if (argc != 3){
        fprintf(stderr,"incorrect usage\n");
        fprintf(stderr, "Usage: cp infile outfile\n");
        return 1;
    }
    /*open the outputfile*/

    outfile = fopen(argv[2], "w");
    if (outprint == NULL){
        fprintf(stderr, "Cannnot open file for writing: %\n", argv[2];)
        return 3;
    }
    /*copy one file to another*/
    /*use fgetc and fputc*/

    do{
        ch = fgetc(infile);
        if (ch != EOF){
            fputc(ch, outfile);
        }
    }while (ch != EOF);
    /*should be done*/

    fclose(infile);
    fclose(outfile);

    return 0;
}