package AlgExpress;

import java.awt.List;
import java.io.*;
import java.util.ArrayList;

public class AlgExpress {

	static final int LIM_LINE=1;
	static final int VAR_LINE=2;
	static final int PLY_LINE=3;

	public static void main(String[] args) throws IOException {

		String inpath="c:\\Users\\synapse\\Desktop\\CODING\\projects\\eclipse\\AlgExpress\\input.txt";
		int num_cases=0;
		int lncnt=0;
		String ln;	
		//CREATE CASE OBJECT ARRAY
		ArrayList<parsin> parsobj = new ArrayList<parsin>();

		ArrayList<String> lns = new ArrayList<String>();

		FileReader fin = new FileReader(inpath);
		BufferedReader bfin = new BufferedReader(fin);

	    while ((ln=bfin.readLine()) != null){
	    	lns.add(new String(ln));
	    	lncnt++;
	    }
	    fin.close();
	    //STORE FIRST LINE AS NUMBER OF CASES
	    num_cases=Integer.parseInt((lns.get(0)).trim());

	    System.out.println("Number of lines, cases - "+lncnt+","+num_cases);
	    //STORE CASE PARAMETERS
	    for(int j=0;j<num_cases;j++){
	    	System.out.println("case number "+j);
	    	parsobj.add(new parsin(lns.get(LIM_LINE+j*num_cases),lns.get(VAR_LINE+j*num_cases),lns.get(PLY_LINE+j*num_cases)));
	    	//System.out.println(parsobj.get(j).plynm);
	    }	
	}
}

class parsin {
	String limits;
	String vars;
	String plynm;
	parsin(String limits, String vars, String plynm) {
		this.limits=limits;
		this.vars=vars;
		this.plynm=plynm;
		//HOW TO BREAK A STRING WITH SPACE AS DELIMITER?
		String[] splimits = limits.split(" ");
		String[] spvars = vars.split(" ");
		String[] spplynm = plynm.split("");
		int[] int_limits = new int[splimits.length];
		int[] int_vars = new int[spvars.length];

		for(int k=0;k<splimits.length;k++){
			int_limits[k]=Integer.parseInt(splimits[k].trim());
		}
		for(int m=0;m<spvars.length;m++){
			int_vars[m]=Integer.parseInt(spvars[m].trim());
		}
		
		int num_vars = int_limits[0];
		System.out.println("Number of variables = "+num_vars);
		//System.out.println(spplynm[3]);
		System.out.println(subplynm(spplynm,int_vars));

		//TO SUBSTITUTE VARS IN THE PLYNM YOU NEED NESTED FOR LOOOPS
		//SINCE ITS COMPLICATED TO WRITE DYNAMIC LOOPS BETTER IDEA MIGHT BE TO RECURSIVELY CALL A FUNCTION

		//PASS PLYNM AND VARS TO FUNCTION
		//FUNCTION NEEDS TO  SUBSTITUTE 
	}
	boolean[] subplynm(String[] exprsn, int[] vars){
		boolean[] xflags = new boolean[vars.length];
		int flagcnt=0;
		for(int i=0;i<exprsn.length;i++){
			if(exprsn[i]=="x"){
				xflags[flagcnt]=true;
				flagcnt++;
			}
		}	
		return xflags;
	}
}