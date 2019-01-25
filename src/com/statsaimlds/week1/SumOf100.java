package com.statsaimlds.week1;
public class SumOf100 {

	public static void main(String[] args) {
		int sum = generateSum(100);
		System.out.println("sum of 100 numbers"+ sum);
		
		sum = generateSumWithFormula(3);
		System.out.println("sum formula of n"+ sum);
	}

	/**
	 * @return
	 */
	private static int generateSum(int num) {
		int sum =0;
		for (int i = 1; i < num+1; i++) {
			sum = sum+i;
		}
		return sum;
	}
	
	
	public static int generateSumWithFormula(int n){
		int sum=0;
		sum=(n*(n+1))/2;
		return sum;
	}

}
