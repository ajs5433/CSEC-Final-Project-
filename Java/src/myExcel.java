package myProject;

import java.io.File;
import java.io.FileInputStream;
//import java.io.FileOutputStream;
//import java.io.ObjectOutputStream;
//import java.io.IOException;
import java.util.Iterator;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
//import org.apache.poi.*;
//import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
//import org.apache.commons.collections4.ListValueMap;

/*
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;
*/
public class myExcel {
	private String filepath;
	private Workbook workbook;
	private static String[][] PAOdata =  new String[20][50];
	
	public myExcel(String filename){
		this.filepath = filename;		
	}
	
	public boolean openfile(){
		boolean check= false;
		workbook = null;
		
		try{
			FileInputStream inputStream = new FileInputStream(new File(filepath));
			workbook = new XSSFWorkbook(inputStream);
			Sheet firstsheet = workbook.getSheetAt(0);
			Iterator<Row> row = firstsheet.iterator();
			
			int r=0,c=0;
			while(row.hasNext()){
				Row nextRow = row.next();
				Iterator<Cell> columnInRow = nextRow.cellIterator();
				c=0;
				
				while(columnInRow.hasNext()){
					Cell cell = columnInRow.next();
					PAOdata[r][c]= cell.getRichStringCellValue().getString();
					System.out.println(cell.getRichStringCellValue().getString());
					c+=1;
				}
				r+=1;
			}
			
			workbook.close();
			inputStream.close();
			
			
		}catch(Exception e){
				System.out.println("There was an error when opening the file and reading its content\n");
				System.err.println(e);
		}
		return check;
	}
	
	public String getName(String letter){
		String name="";
		
		
		return name;
	}
	
	public static void printData(){
		System.out.printf("rows: %d\tcolumns: %d\n", PAOdata[0].length, PAOdata[0][0].length());
		
		for(int row=0; row< PAOdata[0].length; row++){
			for(int column=0;column<PAOdata[0][0].length();column++){
				System.out.print(PAOdata[row][column]+"\t");
			}
			System.out.print("\n");
		}
	}
	/*
	private int getRow(String word){
		int number;
		char letter = word.charAt(0);
		
		switch(letter){
		case('A'):case('a'):number=1;break;
		case('B'):case('b'):number=2;break;
		case('C'):case('c'):number=3;break;
		case('D'):case('d'):number=4;break;
		case('E'):case('e'):number=5;break;
		case('F'):case('f'):number=6;break;
		case('G'):case('g'):number=7;break;
		case('H'):case('h'):number=8;break;
		case('I'):case('i'):number=9;break;
		case('J'):case('j'):number=10;break;
		case('K'):case('k'):number=11;break;
		case('L'):case('l'):number=12;break;
		case('M'):case('m'):number=13;break;
		case('N'):case('n'):number=14;break;
		case('O'):case('o'):number=15;break;
		case('P'):case('p'):number=16;break;
		case('Q'):case('q'):number=17;break;
		case('R'):case('r'):number=18;break;
		case('S'):case('s'):number=19;break;
		case('T'):case('t'):number=20;break;
		case('U'):case('u'):number=21;break;
		case('V'):case('v'):number=22;break;
		case('W'):case('w'):number=23;break;
		case('X'):case('x'):number=24;break;
		case('Y'):case('y'):number=25;break;
		case('Z'):case('z'):number=26;break;
		default: number = 0;
		}
		return number+1;
	}
	
*/
}
