# IT-Canteen

เนื่องจากในปัจจุบัน โรงอาหารคณะเทคโนโลยีสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง มีผู้เข้ามาใช้บริการจำนวนมาก ทำให้เกิดปัญหาด้านต่าง ๆ เช่น
คิวยาวจนบดบังหน้าร้าน, กีดขวางทางเดิน,ไม่ทราบว่าอาหารที่ปรุงเสร็จแล้วเป็นของคิวใด ซึ่งนำไปสู่การหยิบสลับคิวกันได้ จึงต้องการพัฒนาเว็บไซต์ให้มีประสิทธิภาพทั้งในด้านการขาย ด้านการเข้าถึงข้อมูลภายในระบบ และความง่ายในการใช้งาน เพื่อตอบสนองความต้องการของผู้ใช้เว็บ และแก้ปัญหาที่เกิดขึ้น อันเป็นที่มาของการพัฒนาระบบโรงอาหารไอที

## Flow of Events
![](Usecase.jpg)

## How Things Work

จากการวิเคราะห์และออกแบบเพื่อพัฒนาระบบโรงอาหารคณะไอที ในส่วนของผู้ใช้งาน จะประกอบไปด้วย 3 ส่วน ดังนี้

1.Guest : สำหรับผู้ที่ยังไม่เคยลงทะเบียนมาก่อน สามารถเข้าสู่เว็บไซต์เพื่อเข้ามาตรวจสอบคิวและเมนูของแต่ละร้านได้ แต่ถ้าหากต้องการสั่งอาหาร จะต้องเข้าสู่ระบบก่อน

2.User : สมาชิกที่ทำการลงทะเบียนแล้วและต้องการเข้าสู่ระบบเพื่อสั่งอาหาร หรือตรวจสอบคิว สามารถทำได้โดยการลงทะเบียนเข้ามาภายในระบบด้วยบัญชี Google หรือ Facebook หลังจากยืนยันตัวแล้ว ระบบจะนำไปสู่หน้าหลัก

3.Shop : ร้านค้าใด ๆ ที่จะใช้บริการ IT Canteen จะต้องทำการลงทะเบียนก่อน เช่นเดียวกับผู้ใช้ประเภทอื่น จะต้องทำการเลือกช่องทางการเข้าสู่ระบบ

