// // class rataArray{
// //     int arrNilai[];
// //     public rataArray(int [] arrNilai){
// //         this.arrNilai=arrNilai;
// //     }
// // }
// // public void hitungArray(){
// //     int totalNilai = totalNilai + rataArray.arrNilai();


// // }

// // public class array {
// //     public static void main(String[] args) {
        
// //     }    
// // }


// public class sorting {
//     public static void main(String[] args) {
//         int array []= {25, 14, 56, 15, 36, 56, 77, 18, 29, 49,1000};
//         MinMax minmax = new MinMax();
//         minmax.findMinMax(array);
//     }
// }

// class MinMax {
//     void findMinMax(int[] array) {        
//         int max = array[0];
//         int min = array[0];

//         for (int i = 1; i < array.length; i++) {            
//             if (array[i] > max) {
//                 max = array[i];
//             }
//             if (array[i] < min) {
//                 min = array[i];
//             }
//         }

//         System.out.println("Nilai maksimum adalah " + max);
//         System.out.println("Nilai minimum adalah " + min);
//     }
// }

public static void main(String[] args) {
    SequentialSearch  cari = 
}

int SequentialSearch(int arrNilai[], int key)
{	
	for(int i=0; i<arrNilai.length; i++)
	{	
	   if(key == arrNilai[i])
{
return i;
break;
}
	}
	return 0;
}