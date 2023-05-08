# Marvin
Python based Discord bot node for use in automated jupyter-lab workbooks

## Use case, ERP manufacturing assistant
As an assembly worker, I arrive at my workstation and login to the system. I open the Discord app and request my next task from the Marvin node that is assigned to my workstation. Marvin responds promptly and sets the assembly instructions to the screen in front of me.

Next, Marvin sends me a picking list with images of the codes for each of the parts required for the assembly of the cinema LED light. I quickly scan the list and start gathering the required parts. As I collect each part, I take a picture of its unique serial number using my smartphone and send it to Marvin through Discord.

After gathering all the necessary parts, I begin the assembly process. Once the product is complete, I run a quick test to ensure that everything is working correctly. If the product passes the test, I take a picture of the final product and send it to Marvin.

Marvin then generates a PNG file with a QR code and the serial number of the new product. I print out the file using my local label printer and affix the label to the product. Marvin updates the production order in Odoo to reflect the successful completion of the assembly.

In the case of the Apollo/Voyager Battery Mount, I take a picture of the lot number instead of a unique serial number since all the products in the lot will have the same number.

Overall, using the Discord interface with Marvin has made my job as an assembly worker much easier and more efficient. With real-time access to assembly instructions and a straightforward way to communicate with the system, I am able to complete my tasks quickly and accurately.

### Workstation
* ESD Worktable
* Assembly isntructions screen and computer
* BLE label printer
* Cellphone/Barcode Scanner

### Product
Product to be assemebled is Apollo 1 cinema led light that consits of three modules:
1. Apollo 1 Light Module [serial]
1. Apollo 1 Screen Module [serial]
1. Apollo 1x Modular Yoke [lot]
1. Apollo/Voyager Battery Mount [serial]

Assembly:
1. Assemble Light and Screen Module
1. Attach light to Modular Yoke
1. Attach Battery Plate to Mount
1. Run test
1. Attach label

![image](https://user-images.githubusercontent.com/37544886/236781686-35bb7d10-6214-4aae-8ff1-2d684e914c5a.png)

## Use case, Photographer looking for new clients
As a professional photographer, I am always looking for ways to improve my craft. I often use Instagram to find inspiration and see what other photographers are doing. However, this process can be eployed to find new clients - by interacting with people with similar interest. Finding posts that meet specific criteria, such as those with less than 50 likes and certain hashtags can be time-consuming.

To automate this process, I decide to use Marvin. I set up a new channel in Discord and invite Marvin to it. I then provide Marvin with the predefined hashtags and criteria for finding the posts. Marvin scans Instagram regularly for new posts that meet these criteria.

When Marvin finds a post that meets the criteria, it captures the image and uses ChatGPT to generate a positive suggestion for how to try different approaches to lighting for similar subject matter. Marvin generates a list of 50 such suggestions and sends it as text to the Discord channel.

I can then review the list of suggestions and ask Marvin to show me the individual post or provide variations on a specific suggestion. I can also approve or remove suggestions from the list. Once I am satisfied with the list, Marvin attaches a Python script that I can run locally to post the comments on the selected posts.

This process saves me a lot of time and provides me with valuable insights into how I can improve my photography. By automating the process of finding posts that meet specific criteria and generating positive suggestions for lighting, Marvin makes it easier for me to focus on what I do best - taking great photos!

### Workstation
* Discord
* Win/Linux/OSX host to run python script

