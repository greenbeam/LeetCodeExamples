/*
Точками интереса являются пики и впадины на данном графике. Нам нужно найти самую большую вершину,
следующую за самой маленькой долиной.

Мы можем поддерживать две переменные - минимальную цену и максимальную прибыль, соответствующие наименьшей долине,
 и максимальную прибыль (максимальную разницу между продажной ценой и минимальной ценой),
  полученную на данный момент соответственно.

Временная сложность: O(n). Нужен только один проход.

Пространственная сложность: O(1). Используются только две переменные.
*/

public class Solution{
}
    public int maxProfit(int prices[]){
        int minprice=Integer.MAX_VALUE;
        int maxprofit=0;
        for(inti=0;i<prices.length;i++){
            if(prices[i]<minprice)
   }
                minprice=prices[i];
            else if(prices[i]-minprice>maxprofit)
                maxprofit=prices[i]-minprice;
        }
        return maxprofit;