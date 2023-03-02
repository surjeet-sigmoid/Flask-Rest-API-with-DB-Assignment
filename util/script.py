
from database import db
from modal import Product

def create_script():
    prod_obj = Product(status= "OK",  
    copy_right= "Copyright (c) 2019 The New York Times Company.  All Rights Reserved.", 
    num_result = 1,  
    last_modified = "2016-03-11T13:09:01-05:00"
    # results = [ {      
    #              "list_name": "Hardcover Fiction",  
    #              "display_name": "Hardcover Fiction",   
    #              "bestsellers_date": "2016-03-05",      
    #              "published_date": "2016-03-20",    
    #              "rank": 5,      
    #              "rank_last_week": 2,    
    #              "weeks_on_list": 2,     
    #              "asterisk": 0,     
    #              "dagger": 0,      
    #              "amazon_product_url": "http://www.amazon.com/Girls-Guide-Moving-On-Novel-ebook/dp/B00ZNE17B4?tag=thenewyorktim-20",
    #              "isbns": [       
    #                  {         
    #                   "isbn10": 553391925,         
    #                   "isbn13": "9780553391923"       
    #                  }      
    #                  ],      
    #              "book_details": [      
    #                  {         
    #                   "title": "A GIRL'S GUIDE TO MOVING ON",   
    #                   "description": "A mother and her daughter-in-law both leave unhappy marriages and take up with new men.",       
    #                   "contributor": "by Debbie Macomber", 
    #                   "author": "Debbie Macomber",      
    #                   "contributor_note": "",     
    #                   "price": 0,       
    #                   "age_group": "",      
    #                   "publisher": "Ballantine",      
    #                   "primary_isbn13": "9780553391923",      
    #                   "primary_isbn10": 553391925        
    #                   }      
    #                  ],      
    #              "reviews": 
    #                  [        
    #                   {     
    #                    "book_review_link": "",   
    #                    "first_chapter_link": "",      
    #                    "sunday_review_link": "",       
    #                    "article_chapter_link": ""      
    #                    }      
    #                   ]   
    #                  }  
    #            ]
    )
    db.session.add(prod_obj)
    db.session.commit()
    
    
def get_Data():
    get_obj = Product.query.all()
    print(get_obj.prod_obj)