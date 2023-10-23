import { useState, useEffect } from 'react';
import '../styles/ChatBox.css';

export default function ChatBox() {
    // url to the backend
    const url = "http://127.0.0.1:8000/api/handleMessage/";

    // instantiating the first message in the chat
    const [messageList, setMessageList] = useState([{
        "text": "Hi, welcome to [INSERT SHOP NAME HERE], what kind of item are you looking for ?",
        "sender": "AI",
    }]);
    
    // async function that awaits the message returned from the backend
    async function sendMessage(){
        event.preventDefault();

        const YourMessage = document.getElementById("YourMessage");

        // building the json object to be sent to the backend
        var obj = {};
        obj['text'] = YourMessage.value;
        obj['sender'] = "me";
        YourMessage.value = "";

        // updating the message list to be re rendered
        setMessageList(m => m.concat(
            obj
        ));

        //sending the request and awaiting the response
        await fetch(url,{
            "method": "POST",
            "body": JSON.stringify(obj),
            "headers": {
                "Content-type": "application/json; charset=UTF-8"
            },
        }).then(response => {
            return response.json();
        }).then(data => { 
            if("items" in data){ 
                setMessageList(m =>m.concat(
                    {
                        "text": data.text,
                        "items": data.items,
                        "sender": data.sender
                    },)
                );
            }else{
                setMessageList(m =>m.concat(
                    {
                        "text": data.text,
                        "sender": data.sender
                    },)
                );
            }
        });
    }

    // on every update of the messasge list, scroll all the way down
    useEffect(() => {
        const ChatArea = document.getElementById("ChatArea");
        ChatArea.scrollTo(0, ChatArea.scrollHeight);
    }, [messageList]);

    return (
        <div id = "ChatBoxContainer">
            <div id="ChatBoxCard">
                <div id="ChatArea">{
                    messageList.map((message,index)=>{
                        return(
                            <div key={index} className={message.sender == "me"? "FromMe":"FromAI"}>
                                <div className={message.sender == "me"? "TextBubbleMe":"TextBubbleAI"}>{message.text}</div>
                                {"items" in message?
                                <table className="RecommendationTable">
                                    <tr className="RecommendationTableHeader">
                                        <th>Product Name</th>
                                        <th>Description</th>
                                        <th>Price</th>
                                    </tr>
                                    {message.items.map((item,index)=>
                                        <tr key="index">
                                            <td>{item.product_name}</td>
                                            <td>{item.description}</td>
                                            <td className="PriceTag">{item.price}</td>
                                        </tr>
                                    )}
                                </table>:""}
                            </div>
                        )}
                    )
                }</div>
                <form id="TextArea">
                    <input id= "YourMessage" type="text"/>
                    <button id= "SendButton" type="submit" onClick={sendMessage}>SEND</button>
                </form>
            </div>
        </div>
    );
}


