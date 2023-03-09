import java.net.URL;
import java.net.URLConnection;
import java.io.*;
import java.util.*;

public class header{//dont forget this is the program name

    public static void main(String[] Args){
	try{
	    FileWriter file = new FileWriter("OutFile");//this will make a new file
	    PrintWriter OutputFile = new PrintWriter(file);//this should start to print the file
	    
            URL url = new URL("https://www.google.com");//this is a var
	    URLConnection urlconnection = url.openConnection();//this is a var
	    InputStream IS = urlConnection.getInputStream();//this is a var

	    IS.close();//this close the Input Stream
	    OutputFile.print(IS);//this will take you to google
}	catch(Execption e){System.out.println("Error");}//this is a complete try and except
}

}



