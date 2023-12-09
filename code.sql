# Задание 1
# для таблицы Orders есть колонка courierId, 
# courierId: Id курьера - хранится в поле id таблицы Couriers

SELECT C.login, COUNT(*) AS num_of_orders 
FROM "Couriers" AS C 
JOIN "Orders" AS O ON C.id = O."courierId" 
WHERE O."inDelivery" = true 
GROUP BY C.login;


# Задание 2

SELECT track, 
      CASE 
          WHEN finished = true THEN 2 
          WHEN cancelled = true THEN -1 
          WHEN "inDelivery" = true THEN 1 
          ELSE 0 
      END as status 
FROM "Orders";