// Given a class like this:
// class Loan {
//      loan_amount = 1000
//      repayments = [{date: date(2018, 4, 7), amount: 100}, ..., {date: date(2018, 5, 3), amount: 50}]
//      // the array above is only a sample, it could contain more elements. Items are not always sorted.
// }

// Can you write a method Loan.outstanding(day) that returns the amount of money left to repay as at "day"?
// Bonus: can you rewrite the method to use recursion?

class Loan {
    constructor(loan_amount,repayments){
        this.loan_amount = loan_amount;
        this.repayments = repayments.sort(function(a,b){return a.date - b.date});
    }
    outStanding(i,date){
        let repayments =  this.repayments;
        // let loan_amount = this.loan_amount;
        // let sumPaid = 0
        // for(let i=0;i<repayments.length;i++){
        //     if(repayments[i].date<=date){
        //         sumPaid=sumPaid+repayments[i].amount;
        //     }
        //     else{
        //         return loan_amount-sumPaid;
        //     }
        // }
        if(i==repayments.length||repayments[i].date>date){
            return 0;
        }
        return repayments[i].amount+this.outStanding(i+1,date);
    }
}

loan_amount = 1000;
repayments = [{date: new Date(2018, 4, 7), amount: 100}, {date: new Date(2018, 5, 3), amount: 50}];
loan1 = new Loan(loan_amount,repayments)
loan1.outStanding(0,new Date(2018, 5, 7));

