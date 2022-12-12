---DELETE COMMENTS;

--- for publishers table;

delete from Publishers;

insert into Publishers values("89999", "Minotaur Books", "4 Swallow Junction", "3807941719", "apriestley0@cbc.ca", "415056519898648"  );
insert into Publishers values("90001", "Hydra Publications", "810 Knutson Trail", "5576782208",	"fwellbank1@shinystat.com",	"048880910334375" );
insert into Publishers values("90002", "Tuttle Publishing", "581 Westend Place",	"6486841880",	"ethunnerclef2@cornell.edu", "643940028027864"  );
insert into Publishers values("90003", "Lakewater Press", "5785 Bunker Hill Street", "5469607571", "hespinoza3@hud.gov",	"047663528725162"  );
insert into Publishers values("90004", "Minotaur Books", "527 Hoepker Park", "6587081938", "rruffey4@gizmodo.com", "463507128968269"  );
insert into Publishers values("90005", "Lakewater Press", "22 Veith Trail", "7143314445", "cmillins5@mac.com", "882894068558954"  );
insert into Publishers values("90006", "Dover Publications", "695 Leroy Trail", "7707518228", "sluke6@yolasite.com",	"091610624338582"  );
insert into Publishers values("90007", "Blue Swan Publishing", "43 Linden Court", "8733206627", "lkeedwell7@naver.com", "470833852915544"  );
insert into Publishers values("90008", "Coffeetown Press", "0 Bluestem Crossing", "7288375738", "fsignore8@zimbio.com", "246936693545282"  );
insert into Publishers values("90009", "BookPress Publishing", "3906 Pankratz Lane","1623348244", "ajoskowicz9@yellowpages.com",	"943991896599811"  );
insert into Publishers values("90010", "Coffeetown Press", "5 Towne Drive"	,"2615201717","fwatermana@hp.com", "031238576744278"  );




--- for books table;

delete from Books;

insert into Books values("99999", "A World of Curiosities: A Novel", "Louise Penny", 15.99, 20, 654, "mystery", "90000");
insert into Books values("100001", "The Godfather", "Mario Puzo", 50, 70, 1399, "mystery", "90001");
insert into Books values("100002", "The Escape Artist: The Man Who Broke Out of Auschwitz to Warn the World", "Jonathan Freedland", 24.99, 45, 513, "history", "90002");
insert into Books values("100003", "The Wings of Fire: The Dark Secret: A Graphic Novel", "Tui T. Sutherland", 14.28, 45, 212, "fantasy", "90003");
insert into Books values("100004", "The Boys from Biloxi: A Legal Thriller", "John Grisham", 25, 15, 365, "mystery", "90004");
insert into Books values("100005", "Hindu Mythology: A Captivating Guide to Hindu Myths, Hindu Gods, and Hindu Goddesses", "Matt Clayton", 36.25, 40, 784, "history", "90005");
insert into Books values("100006", "The Myths and Gods of India", "Alain Danielou", 55.90, 60, 741, "history", "90006");
insert into Books values("100007", "It Ends with Us", "Colleen Hoover", 10.99, 50, 253, "romance", "90007");
insert into Books values("100008", "It Starts with Us", "Colleen Hoover", 15.99, 20, 354, "romance", "90008");
insert into Books values("100009", "The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", 14.28, 30, 314, "romance", "90009");
insert into Books values("100010", "Fairy Tale", "Stephen King", 45.99, 60, 754, "fantasy", "90010");


--- for users table;

delete from Users;
insert into Users values("admin", "admin");
insert into Users values("user1", "user1");


--- for billing and shipping;

delete from Billing;
insert into Billing values("admin", "58 Northfield Trail" );
insert into Billing values("user1", "2 Ridge Oak Alley");



delete from Shipping;
insert into Shipping values("admin", "58 Northfield Trail");
insert into Shipping values("user1", "1 Cottonwood Center");