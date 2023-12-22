# Write your MySQL query statement below

select tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;