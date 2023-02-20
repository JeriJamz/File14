public class Singleton{

	private static Singleton singleton = new Singleton( );

	private Singleton(){ }//this is a Constructor.A private Constructor it what limits the number of classes

	/*The Static Instance Method*/

	public static Singleton getInstance( ){//this is the actual instance
		return singleton;
	}

	/*Other methods protected by Singleton-ness*/
	protected static void demoMethod( ){//you can put another method here
		System.out.println("demoMetho for singleton");//ok i get the semi-colons
	}

}
