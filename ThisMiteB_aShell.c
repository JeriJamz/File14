//I def took this from a book this but I need it for Jendo. Thatll make sense when ever I fig GUI
//Command Data Structure
//describe a simple command and argument

//I need to learn how to make shell, Dude this is basically a Parser of O.S

struct SimpleCommand{

    //available space for arguments currently allocated
    int _numberofAvailableArguments;

//# of arguments
    int _numberOfArgumnets;

//array of arguements
    char **_arguments;

    SimpleCommand();
    void insertArgument( char * arguement );

};

//describe a complete command with the multiple pipes if any
//and input output redirecion if any
struct Command{

    int _numberOfAvailableCommands;
    int _numberOfSimpleCommands;
    SimpleCommands ** _simpleCommands;
    char * outFile;//Idk if I need to make these
    char * _inputFIle;
    char * _errFile;
    int _background;

    void promt();
    void print();
    void execute();
    void clear();

    void command();
    void insertSimpleCommand(SimpleCommand * simpleCommand);

}

