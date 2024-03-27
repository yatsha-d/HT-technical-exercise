CREATE TABLE company_size_category (
	Symbol VARCHAR(10),
    Shortname VARCHAR(255),
    SizeCategory VARCHAR(10)
);

INSERT INTO company_size_category (Symbol, Shortname, SizeCategory)
select Symbol, Shortname,
	case when Fulltimeemployees between 1 and 5000 then 'Small'
		when Fulltimeemployees between 5001 and 50000 then 'Medium'
        else 'Large'
	end as SizeCategory
from HT_Raw;
