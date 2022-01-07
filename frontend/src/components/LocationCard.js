import React from 'react';
import {Card} from 'react-bootstrap';

export default function LocationCard(props) {
    return (
        <div>
            <Card className='project-card-view'>
            <Card.Body>
                <Card.Title>{props.name}</Card.Title>
                <Card.Text style={{textAlign: "left"}}>
                    <ul>
                        <li>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Commodi, eveniet?</li>
                        <li>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, eaque!</li>
                        <li>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo, provident?</li>
                    </ul>
                </Card.Text>
            </Card.Body>
        </Card>
        </div>
    )
}
