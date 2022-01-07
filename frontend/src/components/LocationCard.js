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
                        <li>{props.thing[0]}</li>
                        <li>{props.thing[1]}</li>
                        <li>{props.thing[2]}</li>
                    </ul>
                </Card.Text>
            </Card.Body>
        </Card>
        </div>
    )
}
