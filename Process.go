//This is the reciept process
//Im having problem with the vari declas. Dont even try rn. Thank you for the opportunity
package main
import("fmt"
       "encoding/json"
        "os"
        "bytes")

type Customer_Copy struct{

     Retail Retail
     Item Item
     Price Price
     Barcode []Barcode

}


type Retail struct{

     RetailName string

}

type Item struct{

     itemName string
     Brand string
     Quantity string

}

type Price struct{

     Cost string

}

type Barcode struct{

     Number string

}

func(r Customer_Copy ) string() string{

     Physical_Copy := r.Retail.RetailName + "\n" + r.Item.itemName + "/" + r.Item.Brand + "\n" + r.Item.Quantity + "\n" + r.Price.Cost 
     for _, Bardi := range r.Barcode{

	Physical_Copy += "\n" + Bardi.Number()

     }

     return Physical_Copy
//     return Bardi

}

func main(){

    Printout := Costomer_Copy {

	fmt.Println("Please put in the details"),//im workin on takin input from a machine
	fmt.Scanln(&RetailName),
        fmt.Scanln(&itemName),
        fmt.Scanln(&Cost),//this should grab the input
        fmt.Scanln(&Number),

    }

    checkError(err)//checks error
    encoder := json.NewEncoder(Printout)
    decoder := json.NewDecoder(Printout)

    for n := 0; n < 1; n++{

	encoder.Encode(Printout)
	var NewPrintout Printout
	decoder.Decode(&NewPrintout)
        fmt.Println(NewPrintout.String())

     }
  os.Exit(0)
}

func checkError(err error){

     if err != nil{

	fmt.Println("Something Went Wrong", err.Error())
        os.Exit(1)

     }

}

