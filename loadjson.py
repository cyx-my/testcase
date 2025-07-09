import json
import re

data = '''
case1:
1. State: <Home Page><Categories: Electronics, Clothing, Groceries><Search Bar: ""><Cart: 0 items><Profile Icon>  
   Action: touch:<Search Bar>

2. State: <Search Input><Text Field: ""><Suggestions: Laptop, Phone, Headphones><Recent: Shoes, Table>  
   Action: set_text:<"Laptop">

3. State: <Search Results><Product: MacBook Pro 16"><Price: ¥15,999><Add to Cart Button><View Product Button>  
   Action: touch:<Add to Cart Button>

4. State: <Cart><Items: MacBook Pro 16 x1><Price: ¥15,999><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Proceed to Checkout Button>

5. State: <Checkout><Shipping Address: 123 Main St><Payment Method: Credit Card><Total: ¥15,999><Place Order Button>  
   Action: touch:<Place Order Button>

6. State: <Order Confirmation><Order ID: #456789><Product: MacBook Pro 16><Price: ¥15,999><Track Order Button>  
   Action: touch:<Track Order Button>

7. State: <Track Order><Status: Dispatched><ETA: 2 Days><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

8. State: <Track Order><Status: In Transit><Location: Shanghai><ETA: 1 Day><Back Button>  
   Action: touch:<Back Button>

9. State: <Cart><Items: MacBook Pro 16 x1><Price: ¥15,999><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

10. State: <Home Page><Categories: Electronics, Clothing, Groceries><Search Bar: ""><Cart: 0 items><Profile Icon>  
    Action: touch:<Profile Icon>

case2:
1. State: <Home Page><Categories: Computers, Books, Appliances><Search Bar: ""><Cart: 0 items><Profile Icon>  
   Action: touch:<Search Bar>

2. State: <Search Input><Text Field: ""><Suggestions: Smartphone, Headphones, Mouse><Recent: Laptop, TV>  
   Action: set_text:<"Smartphone">

3. State: <Search Results><Product: Xiaomi Mi 11"><Price: ¥3,999><Add to Cart Button><View Product Button>  
   Action: touch:<View Product Button>

4. State: <Product Page><Xiaomi Mi 11><Color: Black><Storage: 128GB><Buy Now Button><Add to Cart Button>  
   Action: touch:<Add to Cart Button>

5. State: <Cart><Items: Xiaomi Mi 11 x1><Price: ¥3,999><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Proceed to Checkout Button>

6. State: <Checkout><Shipping Address: 456 Park Ave><Payment Method: Debit Card><Total: ¥3,999><Place Order Button>  
   Action: touch:<Place Order Button>

7. State: <Order Confirmation><Order ID: #789456><Product: Xiaomi Mi 11><Price: ¥3,999><Track Order Button>  
   Action: touch:<Track Order Button>

8. State: <Track Order><Status: Delivered><ETA: Delivered Today><Track Package Button><Return Button>  
   Action: touch:<Track Package Button>

9. State: <Cart><Items: Xiaomi Mi 11 x1><Price: ¥3,999><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

10. State: <Home Page><Categories: Computers, Books, Appliances><Search Bar: ""><Cart: 0 items><Profile Icon>  
    Action: touch:<Profile Icon>

case3:
1. State: <Home Page><Categories: Clothing, Beauty, Home Appliances><Search Bar: ""><Cart: 0 items><Profile Icon>  
   Action: touch:<Search Bar>

2. State: <Search Input><Text Field: ""><Suggestions: Shoes, Jackets, Dresses><Recent: Bags, Laptop>  
   Action: set_text:<"Bags">

3. State: <Search Results><Product: Leather Handbag"><Price: ¥599><Add to Cart Button><View Product Button>  
   Action: touch:<View Product Button>

4. State: <Product Page><Leather Handbag><Color: Brown><Material: Leather><Buy Now Button><Add to Cart Button>  
   Action: touch:<Add to Cart Button>

5. State: <Cart><Items: Leather Handbag x1><Price: ¥599><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Proceed to Checkout Button>

6. State: <Checkout><Shipping Address: 789 High St><Payment Method: Alipay><Total: ¥599><Place Order Button>  
   Action: touch:<Place Order Button>

7. State: <Order Confirmation><Order ID: #112233><Product: Leather Handbag><Price: ¥599><Track Order Button>  
   Action: touch:<Track Order Button>

8. State: <Track Order><Status: In Transit><ETA: 3 Days><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

9. State: <Cart><Items: Leather Handbag x1><Price: ¥599><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

10. State: <Home Page><Categories: Clothing, Beauty, Home Appliances><Search Bar: ""><Cart: 0 items><Profile Icon>  
    Action: touch:<Profile Icon>

case4:
1. State: <Home Page><Categories: Electronics, Furniture, Toys><Search Bar: ""><Cart: 0 items><Profile Icon>  
   Action: touch:<Search Bar>

2. State: <Search Input><Text Field: ""><Suggestions: Washing Machine, Refrigerator, TV><Recent: Phone, Laptop>  
   Action: set_text:<"Washing Machine">

3. State: <Search Results><Product: Haier Washing Machine"><Price: ¥1,599><Add to Cart Button><View Product Button>  
   Action: touch:<View Product Button>

4. State: <Product Page><Haier Washing Machine><Capacity: 8kg><Type: Front Load><Buy Now Button><Add to Cart Button>  
   Action: touch:<Add to Cart Button>

5. State: <Cart><Items: Haier Washing Machine x1><Price: ¥1,599><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Proceed to Checkout Button>

6. State: <Checkout><Shipping Address: 1234 Riverside><Payment Method: WeChat Pay><Total: ¥1,599><Place Order Button>  
   Action: touch:<Place Order Button>

7. State: <Order Confirmation><Order ID: #334455><Product: Haier Washing Machine><Price: ¥1,599><Track Order Button>  
   Action: touch:<Track Order Button>

8. State: <Track Order><Status: Out for Delivery><ETA: 1 Day><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

9. State: <Cart><Items: Haier Washing Machine x1><Price: ¥1,599><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

10. State: <Home Page><Categories: Electronics, Furniture, Toys><Search Bar: ""><Cart: 0 items><Profile Icon>  
    Action: touch:<Profile Icon>

case5:
1. State: <Home Page><Categories: Fashion, Electronics, Groceries><Search Bar: ""><Cart: 0 items><Profile Icon>  
   Action: touch:<Search Bar>

2. State: <Search Input><Text Field: ""><Suggestions: Camera, Shoes, Makeup><Recent: Clothing, Bags>  
   Action: set_text:<"Camera">

3. State: <Search Results><Product: Canon EOS 5D"><Price: ¥6,999><Add to Cart Button><View Product Button>  
   Action: touch:<View Product Button>

4. State: <Product Page><Canon EOS 5D><Lens: 24-70mm><Color: Black><Buy Now Button><Add to Cart Button>  
   Action: touch:<Add to Cart Button>

5. State: <Cart><Items: Canon EOS 5D x1><Price: ¥6,999><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Proceed to Checkout Button>

6. State: <Checkout><Shipping Address: 321 Maple St><Payment Method: Alipay><Total: ¥6,999><Place Order Button>  
   Action: touch:<Place Order Button>

7. State: <Order Confirmation><Order ID: #223344><Product: Canon EOS 5D><Price: ¥6,999><Track Order Button>  
   Action: touch:<Track Order Button>

8. State: <Track Order><Status: Shipped><ETA: 2 Days><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

9. State: <Cart><Items: Canon EOS 5D x1><Price: ¥6,999><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

10. State: <Home Page><Categories: Fashion, Electronics, Groceries><Search Bar: ""><Cart: 0 items><Profile Icon>  
    Action: touch:<Profile Icon>

case6:
1. State: <Home Page><Featured: Flash Sale, Today’s Deals><Cart: 0 items><Profile Icon>  
   Action: touch:<Flash Sale>

2. State: <Flash Sale><Timer: 2:15 left><Product: iPhone 14 - ¥4999><Add to Cart Button><Buy Now Button>  
   Action: touch:<Buy Now Button>

3. State: <Select Payment Method><Balance: ¥2000><Coupon: ¥500><Pay Now Button><Cancel Button>  
   Action: touch:<Pay Now Button>

4. State: <Payment Confirmation><Amount: ¥4499><Transaction ID: #324567><Track Order Button><Back to Home Button>  
   Action: touch:<Track Order Button>

5. State: <Order Status><Status: Preparing for shipment><ETA: 3 Days><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

6. State: <Track Order><Shipping: DHL><Current Location: Guangzhou><ETA: 2 Days><Back Button>  
   Action: touch:<Back Button>

7. State: <Home Page><Featured: Flash Sale, Today’s Deals><Cart: 1 item><Profile Icon>  
   Action: touch:<Cart>

8. State: <Cart><Items: iPhone 14 x1><Price: ¥4999><Proceed to Checkout Button><Remove Item Button>  
   Action: touch:<Remove Item Button>

9. State: <Home Page><Categories: Electronics, Clothing, Groceries><Search Bar: ""><Cart: 0 items><Profile Icon>  
   Action: touch:<Search Bar>

10. State: <Search Input><Text Field: ""><Suggestions: Laptop, Phone, Shoes><Recent: iPhone 14>  
    Action: set_text:<"Laptop">

case7:
1. State: <Home Page><Membership Benefits: Free Shipping, Special Deals><Cart: 0 items><Profile Icon>  
   Action: touch:<Membership Benefits>

2. State: <Membership Page><Exclusive Deals: 20% Off Electronics, 15% Off Fashion><Join Now Button><Close Button>  
   Action: touch:<Join Now Button>

3. State: <Checkout><Member Price: ¥1599><Total with Discount: ¥1399><Shipping Address: 123 Main St><Place Order Button>  
   Action: touch:<Place Order Button>

4. State: <Order Confirmation><Order ID: #998877><Product: Samsung TV 55"><Price: ¥1399><Track Order Button>  
   Action: touch:<Track Order Button>

5. State: <Track Order><Status: In Progress><ETA: 2 Days><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

6. State: <Track Order><Shipping Carrier: FedEx><Current Location: Beijing><ETA: 1 Day><Back Button>  
   Action: touch:<Back Button>

7. State: <Home Page><Featured: Electronics, Membership Deals, Latest Products><Cart: 1 item><Profile Icon>  
   Action: touch:<Cart>

8. State: <Cart><Items: Samsung TV 55" x1><Price: ¥1399><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

9. State: <Home Page><Membership: Active><Cart: 0 items><Search Bar: ""><Profile Icon>  
   Action: touch:<Profile Icon>

10. State: <Profile Page><Membership Status: Active><Payment Methods: Visa, PayPal><Sign Out Button>  
    Action: touch:<Sign Out Button>

case8:
1. State: <Home Page><Pre-Order: Samsung Galaxy S22 - ¥6999><Cart: 0 items><Profile Icon>  
   Action: touch:<Pre-Order>

2. State: <Pre-Order Page><Available: 300 units><Delivery Date: May 10><Pre-order Now Button><Back Button>  
   Action: touch:<Pre-order Now Button>

3. State: <Checkout><Shipping Address: 123 Elm St><Payment Method: WeChat Pay><Total: ¥6999><Place Order Button>  
   Action: touch:<Place Order Button>

4. State: <Order Confirmation><Order ID: #564738><Product: Samsung Galaxy S22><Price: ¥6999><Track Order Button>  
   Action: touch:<Track Order Button>

5. State: <Track Order><Status: Pre-order in Progress><ETA: May 10><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

6. State: <Track Order><Status: Awaiting Shipment><ETA: May 10><Shipping Carrier: Not Available><Back Button>  
   Action: touch:<Back Button>

7. State: <Home Page><Pre-Order: Samsung Galaxy S22 - ¥6999><Cart: 1 item><Profile Icon>  
   Action: touch:<Cart>

8. State: <Cart><Items: Samsung Galaxy S22 x1><Price: ¥6999><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

9. State: <Home Page><Pre-Order: Samsung Galaxy S22 - ¥6999><Cart: 0 items><Profile Icon>  
   Action: touch:<Profile Icon>

10. State: <Profile Page><Order History: Samsung Galaxy S22><Pre-order Status: Awaiting Shipment><Track Order Button>  
    Action: touch:<Track Order Button>

case9:
1. State: <Home Page><Group Buy: Pizza for ¥29, Limited Time Offer><Cart: 0 items><Profile Icon>  
   Action: touch:<Group Buy>

2. State: <Group Buy Page><Deal: Pizza for ¥29 (Normal Price ¥59)><Add to Cart Button><Buy Now Button>  
   Action: touch:<Buy Now Button>

3. State: <Checkout><Shipping Address: 456 Maple St><Payment Method: Credit Card><Total: ¥29><Place Order Button>  
   Action: touch:<Place Order Button>

4. State: <Order Confirmation><Order ID: #223344><Product: Pizza Deal><Price: ¥29><Track Order Button>  
   Action: touch:<Track Order Button>

5. State: <Track Order><Status: Preparing Food><ETA: 20 min><Track Package Button><Cancel Order Button>  
   Action: touch:<Track Package Button>

6. State: <Track Order><Status: Out for Delivery><Location: Local Restaurant><ETA: 10 min><Back Button>  
   Action: touch:<Back Button>

7. State: <Home Page><Group Buy: Pizza for ¥29, Limited Time Offer><Cart: 1 item><Profile Icon>  
   Action: touch:<Cart>

8. State: <Cart><Items: Pizza Deal x1><Price: ¥29><Proceed to Checkout Button><Remove Button>  
   Action: touch:<Remove Button>

9. State: <Home Page><Categories: Food, Electronics, Fashion><Search Bar: ""><Cart: 0 items><Profile Icon>  
   Action: touch:<Profile Icon>

10. State: <Profile Page><Order History: Pizza Deal x1><Track Order Button><Cancel Button>  
    Action: touch:<Track Order Button>
template:
1. State: <Home Page><Categories: [list]><Search Bar: ""><Cart: # items><Profile Icon>

2. State: <Search Input><Text Field: ""><Suggestions: [items]><Recent: [items]>

3. State: <Search Results><Product: [Name]><Price: ¥[Amount]><Add to Cart Button><View Product Button>

4. State: <Product Page><Product: [Name]><Options: Color, Size><Buy Now | Add to Cart Buttons>

5. State: <Cart><Items: [List]><Total: ¥[Amount]><Proceed to Checkout Button><Remove Buttons>

6. State: <Checkout><Shipping Address: [Address]><Payment Method: [Method]><Total: ¥[Amount]><Place Order Button>

7. State: <Order Confirmation><Order ID: #[ID]><Product Summary><Total: ¥[Amount]><Track Order Button>

8. State: <Track Order><Status: [Stage]><ETA: [Date/Time]><Track Package Button><Cancel Order Button>

9. State: <Select Payment Method><Options: Credit Card, Alipay, WeChat><Pay Now Button><Cancel Button>

10. State: <Flash Sale><Countdown: [Time Left]><Deals: [List]><Add to Cart | Buy Now Buttons>

11. State: <Group Buy Page><Deal: [Item]><Discounted Price><Buy Now | Invite Friends Buttons>

12. State: <Pre-Order Page><Product: [Name]><Delivery Date: [Date]><Pre-order Button><Back Button>

13. State: <Membership Page><Benefits: [List]><Join Now Button><Close Button>

14. State: <Profile Page><Order History: [# Items]><Membership Status: [Active/Inactive]><Settings Icon>

15. State: <Order History><Recent Orders: [Items]><Track Order | Reorder Buttons>

16. State: <Cart Empty><Message: "No items in cart"><Shop Now Button><Home Button>

17. State: <Product Variant Selector><Color: [Options]><Size: [Options]><Confirm Selection Button>

18. State: <Review & Rating><Product: [Name]><Star Rating><Text Field: "Write your review"><Submit Button>

19. State: <Address Management><Saved Addresses: [List]><Add New Address Button><Edit/Delete Buttons>

20. State: <Account Settings><Payment Methods | Addresses | Order History><Sign Out Button>

'''
# 1. 分割出所有case
case_blocks = re.split(r"case\d+:", data)
case_headers = re.findall(r"(case\d+):", data)

cases = []
template_lines = [
    "<Home Page><Categories: [list]><Search Bar: \"\"><Cart: # items><Profile Icon>",
    "<Search Input><Text Field: \"\"><Suggestions: [items]><Recent: [items]>",
    "<Search Results><Product: [Name]><Price: ¥[Amount]><Add to Cart Button><View Product Button>",
    "<Product Page><Product: [Name]><Options: Color, Size><Buy Now | Add to Cart Buttons>",
    "<Cart><Items: [List]><Total: ¥[Amount]><Proceed to Checkout Button><Remove Buttons>",
    "<Checkout><Shipping Address: [Address]><Payment Method: [Method]><Total: ¥[Amount]><Place Order Button>",
    "<Order Confirmation><Order ID: #[ID]><Product Summary><Total: ¥[Amount]><Track Order Button>",
    "<Track Order><Status: [Stage]><ETA: [Date/Time]><Track Package Button><Cancel Order Button>",
    "<Select Payment Method><Options: Credit Card, Alipay, WeChat><Pay Now Button><Cancel Button>",
    "<Flash Sale><Countdown: [Time Left]><Deals: [List]><Add to Cart | Buy Now Buttons>",
    "<Group Buy Page><Deal: [Item]><Discounted Price><Buy Now | Invite Friends Buttons>",
    "<Pre-Order Page><Product: [Name]><Delivery Date: [Date]><Pre-order Button><Back Button>",
    "<Membership Page><Benefits: [List]><Join Now Button><Close Button>",
    "<Profile Page><Order History: [# Items]><Membership Status: [Active/Inactive]><Settings Icon>",
    "<Order History><Recent Orders: [Items]><Track Order | Reorder Buttons>",
    "<Cart Empty><Message: \"No items in cart\"><Shop Now Button><Home Button>",
    "<Product Variant Selector><Color: [Options]><Size: [Options]><Confirm Selection Button>",
    "<Review & Rating><Product: [Name]><Star Rating><Text Field: \"Write your review\"><Submit Button>",
    "<Address Management><Saved Addresses: [List]><Add New Address Button><Edit/Delete Buttons>",
    "<Account Settings><Payment Methods | Addresses | Order History><Sign Out Button>"
]




for i, block in enumerate(case_blocks[1:]):
    lines = [line.strip() for line in block.strip().split("\n") if line.strip()]
    steps = []
    for j in range(0, len(lines), 2):
        state_line = lines[j]
        action_line = lines[j + 1] if j + 1 < len(lines) else ""
        # 提取 State 和 Action
        state = re.sub(r'^.*State:\s*', '', state_line)
        action = re.sub(r'^.*Action:\s*', '', action_line)
        steps.append({"state": state, "action": action})
    cases.append({
        "case_id": case_headers[i],
        "steps": steps
    })

final_json = {
    "app": "amazon",
    "template":template_lines,
    "cases": cases
}

# 保存为 JSON 文件
with open("amazon_cases.json", "w", encoding="utf-8") as f:
    json.dump(final_json, f, indent=2, ensure_ascii=False)

