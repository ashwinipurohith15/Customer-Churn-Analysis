use churn;
select * from churn;
select * from customers;
select * from Subscriptions;
select * from transactions;

-- Reterive all customers from north america region
select FirstName,LastName,customerid,region
from customers
where region='North America';  

select count(*)
from customers
where region='North America';  

-- Total numbers of customers
select count(*) as Total_Customers
from customers;

-- Active Customers on the platform
select count(*)
from customers
where Status = 'Active';

-- Customers who joined the platform after 1 january 2021
 
SELECT count(*)
FROM   customers
WHERE  JoinDate >= date('01-01-2021');

select * from customers;
-- Customers who joind the platform in 2022

select count(*)
from customers
where JoinDate like '%2022';

-- Name of the Customer who have the email id as 'john.doe@example.com'
select *
from customers
where Email='john.doe@example.com';

-- Number of customers who have taken annual subscrpitions
select * from subscriptions;
select * from customers;
select count(*)as Total_subscriptions
from subscriptions
where PlanType='Annual';

-- Check the customer oscar Wright planType

select *
from subscriptions s
join customers c on s.CustomerID = c.CustomerID
where c.FirstName='Oscar' and c.LastName='Wright';

-- Calculate the average amount of all transactions
select * from transactions;

select avg(Amount)as Average_amount
from transactions;

-- Retrieve all transactions where the amount is greater than $100
Select count(*)
from transactions
where Amount>100;

-- Retrieve all transactions made by a customer with CustomerID 10
select count(*) 
from transactions
where CustomerID ='10';

-- Retrieve all transactions with the first and last name , Transactions id and Transaction Amount of the customers who the transactions.
select FirstName,LastName,TransactionID,Amount
from transactions t
join customers c on t.CustomerID = c.CustomerID;

-- Retrieve all the reasons for churn listed.
select * from churn;
select distinct Reason from churn;

-- Retrieve the major reason fot the customer churn
select Reason,count(customerID) from churn group by reason;

-- Retrieve the customer details along with subscription details

select c.CustomerID,c.FirstName,c.LastName,s.SubscriptionID,s.PlanType
from customers c
Join subscriptions s on c.CustomerID = s.CustomerID;

select PlanType,count(CustomerID) as Customer_Count
from subscriptions
group by PlanType;

-- Retrieve how many active customers who have an annual subscriptions 
 Select * from customers;

select count(C.CustomerID)as Total_Customers,C.status, s.PlanType
from subscriptions s
join Customers C on s.CustomerID = C.CustomerID
where C.Status='Active' and s.PlanType='Annual';






